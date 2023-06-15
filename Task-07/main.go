package main

import (
	"syscall/js"
)

var count int

// Implement the functions here

func increment(this js.Value, args []js.Value) interface{} {
	count++
    return count
}

func reset(this js.Value, args []js.Value) interface{} {
    count=0
    return count
}

func decrement(this js.Value, args []js.Value) interface{} {
	count--
    return count
}

func main() {
	c := make(chan bool)
	js.Global().Set("increment", js.FuncOf(increment))
	js.Global().Set("reset", js.FuncOf(reset))
	js.Global().Set("decrement", js.FuncOf(decrement))

	<-c
}