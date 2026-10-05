class OcticAiAgent < Formula
    include Language::Python::Virtualenv
  
    desc "Octic AI Agent - AI agent framework"
    homepage "https://github.com/Aravindh-dev12/octic-Agent"
    url "https://github.com/MervinPraison/PraisonAI/archive/refs/tags/v4.7.12.tar.gz"
    sha256 `curl -sL https://github.com/MervinPraison/PraisonAI/archive/refs/tags/v4.7.12.tar.gz | shasum -a 256`.split.first
    license "MIT"
  
    depends_on "python@3.11"
  
    def install
      virtualenv_install_with_resources
    end
  
    test do
      system "#{bin}/octic-ai-agent", "--version"
    end
  end
  