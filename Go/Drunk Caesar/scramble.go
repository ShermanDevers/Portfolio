package main

import (
	"math/rand"
)

const alphabet = "abcdefghijklmnopqrstuvwxyz"

func scramble(message string) string {
	scrambled := ""
	for i := 0; i < len(message); i++ {
		if string(message[i]) == " " || string(message[i]) == "\n" {
			scrambled += " "
		} else {
			var newIndex = rand.Intn(len(alphabet))
			var newLetter = string(alphabet[newIndex])
			scrambled += newLetter
		}
		
	}
	return scrambled
}
