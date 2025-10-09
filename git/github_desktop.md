# Verified Commits
```
# Install GPG
brew install gnupg

# Generate key
gpg --full-generate-key
# Key type: RSA and RSA
# Key size: 4096
# Expiration: your choice
# Name/email: must match your GitHub email

# Check the key
gpg --list-secret-keys --keyid-format=long
# Copy the key ID (e.g. ABC123DEF4567890).
# Right after "sec   rsa4096/<15_numbers_and_letters> 2025-10-09 [SC]"

# Set the key locally
git config --global user.signingkey ABC123DEF4567890
git config --global commit.gpgsign true

# Export key
gpg --armor --export ABC123DEF4567890

# Copy the key in GitHub SSH and GPG Keys

# Check if the keys are locally store in GitHub Desktop > Settings > git > edit your global Git config file.
```