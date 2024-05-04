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

If you don't want the server to refresh when you make changes to files then use

```bash
node server.cjs
```
__For development work I highly recommend always using nodemon rather than node.__


Both will currently start the backend server at http://localhost:8000/ (I just selected port 8000 at the time of writing this).


This port is subject to change and the port can be found in server.js file at the app.listen() call.


## Running The React App

make a new terminal and cd into the Sol/src folder and run
```bash
npm run dev
```

This will serve the react frontend on http://localhost:5173/ default unless you are running another app on that port (I think) 


Sometimes you will get EACCESS errors and so,

```bash
sudo npm run dev
```

may be needed.

Link to Web Application: https://sol-ec-464-team-15.netlify.app/
