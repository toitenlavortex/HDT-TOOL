# Changelog

## [1.0.1] - 2025-05-07
### Fixed
- **Error downloading or running script**: Fixed an issue where the script couldn't download or run due to the `'charmap' codec can't encode character '\U0001f602'`. This occurred when encountering special characters (e.g., emoji) that couldn't be encoded properly in the system.
- Updated encoding to ensure better compatibility when writing special characters to a file (using `UTF-8`).

![image](https://github.com/user-attachments/assets/1a6d2aae-80a6-4a20-87dc-0baa89d9a45e)
