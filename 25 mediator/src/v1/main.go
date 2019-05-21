package main

import (
	"v1/country"
	"v1/united_nations"
)

func main() {
	usa := country.USA{}
	iraq := country.Iraq{}
	sc := united_nations.SecurityCouncil{}
	sc.SetCountry(usa, iraq)
	usa.SetMediator(sc)
	iraq.SetMediator(sc)

	usa.SendMessage("Hello bro.")
	iraq.SendMessage("...")

}