package main

import (
	"fmt"
	"math/rand"
)
// Generates a code with a given length
func generate(length int) string {
	code := ""
	for i := 0; i < length; i++ {
		code += fmt.Sprintf("%v", rand.Intn(11))
	}
	if len(code) == length {
		return code
	} else {
		return code[:length]
	}
}

func main() {
	var length int
	fmt.Print("How long do you want your code to be?: ")
	fmt.Scan(&length)
	fmt.Println(generate(length))
}


