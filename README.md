# IFE_Python
AI-based video processing software using Qt with PySide6

Author: [Farruck Ahamed Tusar](https://github.com/farruck-tusar)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PySide6.

```bash
pip install PySide6
```

## Usage
```python
from PySide6 import QtWidgets

# add 'QIcon'
from PySide6.QtGui import QIcon

# add 'QDir'
from PySide6.QtCore import QDir

# import generated python file from .ui files
from ui_mainwindow import Ui_MainWindow
```
## Key Features
* Video Frame Processing
* Integrate DL and feature-based object detection algorithms
* Modular architecture to support reusability
* Data Serialization
* Heatmap feature to highlight frames with detected objects
* Cross-Platform Support
