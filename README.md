# EC463-Senior-Design-Stand-Alone-Solar-Project-Github

# Run Sol

Sol is a MERN stack web application that will be used to monitor a stand alone solar power plant

## How to run 

## Dependencies

Install node.js
Install the package manager npm

Use the package manager npm to install the dependencies in Sol/package.json

(note: don't put the angle brackets into the terminal). 

```bash
npm install <dependency>
```
Sometimes you will get EACCESS errors and so,

```bash
sudo npm install <dependency>
```

may be needed.

## Running The backend Server

Enter a terminal and cd into Sol/src/backend before running:

__(HIGHLY RECOMMENDED):__
for responsive development (nodemon restarts the server whenever you make changes to files) 
```bash
nodemon server.cjs
```


```bash
node server.cjs
```
Both will currently start the backend server at http://localhost:8000/ (I just selected port 8000 at the time of writing this.

This port is subject to change and the port can be found in server.js fileat the app.listen() call.


## Running The React App

make a new terminal and cd into the Sol/src folder and run
```bash
npm run dev
```

This will serve the react front end on http://localhost:5173/



