package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	var clientConnections = []net.Conn{}
	listener, err := net.Listen("tcp", ":8080")
	fmt.Println("Server is running on port 8080")
	for {
		if err != nil {
			fmt.Println(err)
			break
		}
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println(err)
			break
		} else {
			clientConnections = append(clientConnections, conn)
			go handleConnection(conn, clientConnections)

		}
	}
	listener.Close()
}

func handleConnection(conn net.Conn, clientConnections []net.Conn) {
	fmt.Printf("%v connected\n", conn.RemoteAddr())
	go actionOption(clientConnections)
}

func connections(clientConnections []net.Conn) {
	fmt.Printf("%v Client(s) connected\n", len(clientConnections))

}

func actionOption(clientConnections []net.Conn) {
	for {
		fmt.Print("What would you like to do?: ")
		inreader := bufio.NewReader(os.Stdin)
		cmd, _ := inreader.ReadString('\n')
		actionArray := strings.Fields(cmd)
		switch actionArray[0] {
		case "exit":
			fmt.Println("Exiting")
			os.Exit(0)
		case "list":
			fmt.Println("Listing")
			connections(clientConnections)
		case "send":
			sendCommand(clientConnections)

		default:
			fmt.Println("Invalid option")
		}
	}

}

func sendCommand(clientConnections []net.Conn) {
	
	
	fmt.Print(">")
	inreader := bufio.NewReader(os.Stdin)
	command, _ := inreader.ReadString('\n')
	for _, c := range clientConnections {
		c.Write([]byte(command))
		buff := make([]byte, 1024)
		nbytes, err := c.Read(buff[:])
		if err != nil {
			fmt.Println(err)
			return
		} else {
			fmt.Printf("From %v\n",c.RemoteAddr())
			fmt.Println(string(buff[:nbytes]))
		}
	}


}
