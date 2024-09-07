DenGuard Antivirus
DenGuard Antivirus is a comprehensive antivirus solution that integrates both powerful backend functionality and a user-friendly graphical interface (GUI). This project offers features like malware scanning, virus removal, junk file cleaning, and RAM optimization, making it a valuable tool for enhancing both system security and performance.

Features
1. Virus Scanner
The virus scanner identifies malware by computing the SHA256 hash of each file in a specified directory. This hash is compared against a predefined list of known malware hashes stored in the virusHash.denvit file. If a match is found, the malware is flagged, and its details are logged from the virusInfo.denvit file.

This technique is efficient and reliable for detecting malware based on known signatures, ensuring quick identification of malicious files.

2. Virus Remover
The virus remover deletes flagged files detected during the scanning process. It checks the paths of the infected files stored in virusPath and removes them from the system. If no malware is detected, it reports that the system is clean.

This feature guarantees the removal of harmful files from the system to maintain a safe computing environment.

3. Junk File Remover
This function cleans temporary files from system directories like C:\\Windows\\Temp, which often accumulate unnecessary files over time. It helps free up disk space and ensures a more efficient system by removing both junk files and empty folders.

Regular removal of these files helps improve the system's overall performance.

4. RAM Booster
The RAM booster kills unnecessary background processes that consume memory, such as browsers, media players, and office applications. By terminating these processes, the program frees up system memory, resulting in improved performance.

This is especially useful for users experiencing slowdowns due to excessive memory usage by idle processes.

Graphical User Interface (GUI)
DenGuard Antivirus features a simple and intuitive GUI built using Python's Tkinter library. The GUI allows users to interact with the antivirus engine effortlessly.

1. Design and Layout
The interface is designed with fixed dimensions (1000x600 pixels) and features the DenGuard logo, a progress bar, and several buttons for user control. It offers an intuitive layout that makes the antivirus tool easy to use for both technical and non-technical users.

2. Progress Bar and Status Display
A progress bar is integrated to visually represent the status of ongoing tasks like virus scanning. The percentage of completion is displayed alongside the bar, providing real-time feedback to the user.

3. Functionality Buttons
Four primary buttons allow the user to initiate specific tasks:

Virus Scanner: Starts malware scanning.
Virus Remover: Deletes flagged malware files.
RAM Booster: Optimizes memory by killing idle processes.
Junk File Remover: Cleans up temporary files to free disk space.
There is also a Quit button to close the application.

4. Automated Operations
The step() function automates the process by running the virus scanner, virus remover, RAM booster, and junk file remover in sequence with a single button press. This makes it easy for users to perform a complete system scan without manually running each operation.

Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/DenGuardAntivirus.git
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python main.py
Contributing
Contributions are welcome! Feel free to open issues or create pull requests for any improvements or bug fixes.

This project provides an efficient, user-friendly antivirus solution with both essential security features and system optimization, making it accessible to a wide range of users.
![](https://github.com/shraddhapandey100/ProjectExhibition_2/blob/paneltime/DenGuardProject/AntiviursProject/GUI.png)
![](https://github.com/shraddhapandey100/ProjectExhibition_2/blob/paneltime/DenGuardProject/AntiviursProject/GUI_1.png)

![](https://github.com/shraddhapandey100/DenGuard/blob/paneltime/Architecture%20.png)
