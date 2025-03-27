# Telegram Mini App Image Converter Backend

This backend supports image conversion (resize, compress, change format) for your Telegram Mini App frontend.

- Endpoint: `/convert`
- Method: POST
- Accepts: `file`, `format`, `scale`, `quality`
- Returns: Converted image as a file download