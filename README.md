Uses the AES symmetric encryption algorithm to encrypt messages. AES is an industry standard and very secure when implemented correctly.

Encryption keys are randomly generated 256-bit keys. This makes brute-forcing the keys infeasible. Longer, more random keys enhance security.

By using unique random keys for each message, it ensures that even if one message is cracked, it does not compromise other messages encrypted with other keys.

The GCM mode is used with AES which provides both confidentiality through encryption as well as integrity and authenticity checking. This prevents tampering with encrypted messages.

Key exchange is handled by base64 encoding the raw binary AES keys into ASCII text which allows the transfer of the keys through email, chat, etc.

Both the AES encrypted messages as well as the keys are base64 encoded to convert the binary data to readable text before transmission or storage.
