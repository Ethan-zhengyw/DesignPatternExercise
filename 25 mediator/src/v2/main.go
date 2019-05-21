package main

import (
	"v2/country"
)

func main() {
	usa := &country.USA{}
	iraq := &country.Iraq{}
	sc := &country.SecurityCouncil{}
	sc.SetCountry(usa, iraq)
	usa.SetMediator(sc)
	iraq.SetMediator(sc)

	usa.SendMessage("Hello bro.")
	iraq.SendMessage("...")

}