package country

import "fmt"

type SecurityCouncil struct {
	usa *USA
	iraq *Iraq
}

// implement interface IUnitedNations
func (sc *SecurityCouncil) sendMessage(m string, c ICountry) {
	// switch v := c.(type) {
	// case country.USA:
	// 	sc.iraq.GetMessage(m)
	// case country.Iraq:
	// 	sc.usa.GetMessage(m)
	// default:
	// 	fmt.Println("Illegal country!")
	// }

	if _, ok := c.(USA); ok {
		sc.iraq.GetMessage(m)
	} else if _, ok := c.(Iraq); ok {
		sc.usa.GetMessage(m)
	} else {
		fmt.Println("Illegal country!")
	}

}

func (sc SecurityCouncil) SetCountry(usa *USA, iraq *Iraq) {
	sc.usa = usa
	sc.iraq = iraq
}