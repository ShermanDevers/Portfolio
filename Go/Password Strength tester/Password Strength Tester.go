package main

import (
	"fmt"
	"strings"
)

func lengthTest(passwd, passed, failed string) string {
	minimumLength := 12
	lengthResult := ""
	if len(passwd) >= minimumLength {
		lengthResult = passed
		return lengthResult
	} else {
		lengthResult = failed
		return lengthResult
	}
}

func specialTest(passwd, passed, failed string) string {
	specialResult := ""
	var specialChara = "!#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
	if strings.ContainsAny(passwd, specialChara) {
		specialResult = passed
		return specialResult
	} else {
		specialResult = failed
		return specialResult
	}

}

func numbersTest(passwd, passed, failed string) string {
	numbersResult := ""
	var numbers = "0123456789"
	if strings.ContainsAny(passwd, numbers) {
		numbersResult = passed
		return numbersResult
	} else {
		numbersResult = failed
		return numbersResult
	}

}

func main() {
	var passed = "✓"
	var failed = "✗"

	var passToTest string
	fmt.Print("Enter a password to test: ")
	fmt.Scan(&passToTest)
	fmt.Printf("Length: %s\n", lengthTest(passToTest, passed, failed))
	fmt.Printf("Special Characters: %s\n", specialTest(passToTest, passed, failed))
	fmt.Printf("Numbers: %s\n", numbersTest(passToTest, passed, failed))
}
