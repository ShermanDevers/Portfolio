package main

import (
	"fmt"
	"strings"
)

func lengthTest(passwd, passed, failed string) string {
	minimumLength := 12
	length_Test := ""
	if len(passwd) >= minimumLength {
		length_Test = passed
		return length_Test
	} else {
		length_Test = failed
		return length_Test
	}
}

func specialTest(passwd, passed, failed string) string {
	special_Test := ""
	var specialChara string = "!#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
	if strings.ContainsAny(passwd, specialChara) {
		special_Test = passed
		return special_Test
	} else {
		special_Test = failed
		return special_Test
	}

}

func numbersTest(passwd, passed, failed string) string {
	numbers_Test := ""
	var numbers string = "0123456789"
	if strings.ContainsAny(passwd, numbers) {
		numbers_Test = passed
		return numbers_Test
	} else {
		numbers_Test = failed
		return numbers_Test
	}

}

func main() {
	var passed = "✓"
	var failed = "✗"

	var passwd_to_test string
	fmt.Print("Enter a password to test: ")
	fmt.Scan(&passwd_to_test)
	fmt.Printf("Length: %s\n", lengthTest(passwd_to_test, passed, failed))
	fmt.Printf("Special Characters: %s\n", specialTest(passwd_to_test, passed, failed))
	fmt.Printf("Numbers: %s\n", numbersTest(passwd_to_test, passed, failed))
}
