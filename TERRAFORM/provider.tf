terraform {
  required_providers {
    hyperfabric = {
      source = "cisco-open/hyperfabric"
    }
  }
}

provider "hyperfabric" {
   token = "your_token_goes_here"
   retries = 2
   label = "terraform"
  # proxy_url = "http://proxy.esl.cisco.com"
  # proxy_creds = "username:password"
   auto_commit = true
}
