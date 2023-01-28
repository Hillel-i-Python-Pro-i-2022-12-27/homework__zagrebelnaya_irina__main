## 📝Homework 4
Simple code with simple logic in a Docker container using random name generation [Faker](https://pypi.org/search/?q=faker).
Displays the student's name with grade and description. 
### ▶️Run
Run homework without docker.
```shell
make homework-i-run
```
### 🗑️Purge
```shell
make homework-i-purge
```
## 🛠️Dev
### ⚙️Initialize dev
```shell
make init-dev
```
***
## 🐳Docker
Use services in dockers.
### ▶️Run
Make all actions needed for run homework from zero.
```shell
make d-homework-i-run
```
### ⏹️Stop
Stop services
```shell
make d-stop
```
### 🗑️Purge
Purge all data related with services
```shell
make d-homework-i-purge
```