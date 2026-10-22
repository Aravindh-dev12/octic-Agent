/**
 * `octo` binary entry point.
 *
 * Parses argv, builds a request frame, sends it via the picked transport,
 * formats the response, exits non-zero on error.
 *
 * Usage:
 *   octo <resource> <verb> [target] [--key value ...] [--stdin-json] [--json]
 *
 * Examples:
 *   octo groups list
 *   octo groups get abc123
 *   octo groups create --name foo --folder bar
 *   octo groups update abc123 --name baz
 *   octo help
 *   octo groups help
 */
import { randomUUID } from 'crypto';

import { formatResponse } from './format.js';
import type { RequestFrame } from './frame.js';
import { parseArgv } from './parse-argv.js';
import { SocketTransport } from './socket-client.js';
import { readStdinJsonArgs, StdinJsonInputError } from './stdin-json.js';
import type { Transport } from './transport.js';
import { formatTransportError } from './transport-errors.js';

async function main(): Promise<void> {
  const argv = process.argv.slice(2);

  if (argv.length === 0 || argv[0] === '--help' || argv[0] === '-h') {
    printUsage();
    process.exit(0);
  }

  const { command, args, json, stdinJson } = parseArgv(argv);
  if (command.length === 0) {
    process.stderr.write('octo: missing command\n');
    printUsage();
    process.exit(2);
  }

  let requestArgs = args;
  if (stdinJson) {
    if (process.stdin.isTTY) {
      // Reading a TTY would silently block until the user types Ctrl-D.
      process.stderr.write('octo: --stdin-json requires piped stdin (e.g. `echo {...} | octo ...`)\n');
      process.exit(2);
    }
    try {
      requestArgs = await readStdinJsonArgs(args);
    } catch (err) {
      if (err instanceof StdinJsonInputError) {
        process.stderr.write(`octo: ${err.message}\n`);
        process.exit(2);
      }
      throw err;
    }
  }

  const frame: RequestFrame = {
    id: randomUUID(),
    command,
    args: requestArgs,
  };

  const transport = pickTransport();
  let res;
  try {
    res = await transport.send(frame);
  } catch (e) {
    process.stderr.write(formatTransportError(e));
    process.exit(2);
  }

  const output = formatResponse(res, { json });
  // Exit only after stdout drains: process.exit() discards buffered pipe
  // writes, silently truncating any response past the 64KB pipe buffer
  process.stdout.write(output, () => process.exit(res.ok ? 0 : 1));
}

function pickTransport(): Transport {
  return new SocketTransport();
}

function printUsage(): void {
  process.stdout.write(
    [
      'Usage: octo <resource> <verb> [target] [--key value ...] [--stdin-json] [--json]',
      '',
      '  --stdin-json  Read one bounded JSON object from stdin and merge it with argv flags.',
      '',
      'Run `octo help` to list available resources and commands.',
      '',
    ].join('\n'),
  );
}

main().catch((err) => {
  process.stderr.write(`octo: unexpected error: ${err instanceof Error ? err.message : String(err)}\n`);
  process.exit(2);
});
