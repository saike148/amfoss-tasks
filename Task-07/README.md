### Go-Wasm

#### main.go
1. In the main.go file, I added functionality for increment,decrement and reset buttons

- Added a wasm_exec.js file.

#### index.html
1. Three JavaScript functions were added: `incrementCounter()`, `resetCounter()`, and `decrementCounter()` - responsible for calling the corresponding functions in the WebAssembly module and updating the counter value which is then displayed using `setCounterValue()` function.
2. The buttons were given `onclick()` attribute to call the respective functions.

#### Running
1. The `main.go` file was made into built into `main.wasm` file using the command `GOARCH=wasm GOOS=js go build -o main.wasm main.go`
2. `index.html` was successfully hostel onto the browser to show a working counter similar to the one given in `demo.gif`.