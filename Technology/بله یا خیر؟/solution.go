package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scanln(&s)

	na := strings.Index(s, "na")
	areh := strings.Index(s, "areh")
	bale := strings.Index(s, "bale")
	kheir := strings.Index(s, "kheir")

	countna := strings.Count(s, "na")
	countareh := strings.Count(s, "areh")
	countbale := strings.Count(s, "bale")
	countkheir := strings.Count(s, "kheir")


	if countareh != countna || countkheir != countbale || areh > na || bale > kheir {
		fmt.Println("NO")
		return
	}

	if na > kheir && areh > bale  {
		fmt.Println("NO")
		return
	}
	fmt.Println("YES")
}