# Python Brute Force Attack with Tor and True Parallelism

This repository contains Python code examples for implementing brute force attacks while utilizing the Tor network with true parallelism. It can be used for educational purposes and security testing, provided you have the necessary permissions and adhere to ethical guidelines.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this code, ensure you have the following prerequisites:

- Python 3.x
- The following Python libraries:
  - `requests` (you can install it using `pip install requests`)
- Tor installed and running on your system.

## Examples

Here are some examples of how to use this code:

### 1. Adjust credentials accordingly to the target website:

```credentials = {'account': 'example', 'password': password}```

### 2. Set the target URL
```target_url = "https://example.com/login"```

### 3. Specify the directory containing password lists
```directory = "C:\\path\\to\\passwords\\"```

### 4. Customize the number of concurrent workers in the ThreadPoolExecutor to optimize performance.
Adjust the number of concurrent workers based on your system's capabilities  
```ThreadPoolExecutor(max_workers=6000) as executor:```  
```    futures = {executor.submit(try_password, password, tor_client) for password in all_passwords} ```

## Contributing

Contributions to this repository are welcome. Feel free to open issues, submit pull requests, or provide suggestions for improvements.

## License

This project is licensed under the MIT License.

## Note: This code is intended for educational and ethical purposes only. Unauthorized use for malicious activities is strictly prohibited
