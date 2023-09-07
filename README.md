# EMLEddtech-backend

# To set up for development

1.  **Install Python**:
    
    Make sure you have Python installed on your system. If not, you can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
    (**Recommended:** Install Python version 3.11.0)
2. **Recommended: Create directory to hold backend in.**
3. **Clone repository by running command**
	```
	git clone https://github.com/EliteML/EMLEddtech-backend.git
	```
4.  **Enter the cloned repository using command**
	```
	cd EMLEddtech-backend
	```
5.  **Set up virtual environment(optional but HIGHLY recommended)**
	```
	python -m venv env
	# On mac use: 
	source env/bin/activate  
	# On Windows use: 
	.\env\Scripts\activate
	```
	**Note**: Must activate every time you enter repository and the virtual environment is not activated.
6. **Install dependencies**
	```
	pip install -r requirements.txt
	```
7. **Now you can run the flask server using**
	```
	 flask run
	```