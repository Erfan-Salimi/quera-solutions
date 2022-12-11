package main

import (
	"fmt"
	"strconv"
)

func main() {
	var w int
	var x string
	fmt.Scanln(w)
	fmt.Println(HelloCodeCup(w))
	fmt.Println(x)
}
func HelloCodeCup(n int) string {
	str := "Hello CodeCup "
	x := str + strconv.Itoa(n)
	return x
}
