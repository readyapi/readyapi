# `UploadFile` class

You can define *path operation function* parameters to be of the type `UploadFile` to receive files from the request.

You can import it directly from `readyapi`:

```python
from readyapi import UploadFile
```

::: readyapi.UploadFile
    options:
        members:
            - file
            - filename
            - size
            - headers
            - content_type
            - read
            - write
            - seek
            - close
