package main

import (
	"fmt"
	"bufio"
	"os"
)


func main() {

	fmt.Println("mmmm                        #               mmm                             ")
	fmt.Println("#   'm  m mm  m   m  m mm   #   m         m'   '  mmm    mmm    mmm    mmm   m mm")
	fmt.Println("#    #  #'  ' #   #  #'  #  # m'          #      '   #  #'  #  #   '  '   #  #'  '")
	fmt.Println("#    #  #     #   #  #   #  #'#           #      m'''#  #'''#   '''m  m'''#  #")
	fmt.Println("#mmm'   #     'mm'#  #   #  #  'm          'mmm' 'mm'#  '#mm'  'mmm'  'mm'#  #")
	fmt.Println("")
	fmt.Println("                   The Inconsistent Cipher                                  ")
	fmt.Println("")

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Type a message to scramble: ")
	message, _ := reader.ReadString('\n')
	fmt.Println(scramble(message))
}