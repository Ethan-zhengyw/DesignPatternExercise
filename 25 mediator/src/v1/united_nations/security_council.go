package united_nations

import "fmt"
import "v1/country"

type SecurityCouncil struct {
	usa country.USA
	iraq country.Iraq
}

// implement interface IUnitedNations
func (sc SecurityCouncil) sendMessage(m string, c country.ICountry) {
	// switch v := c.(type) {
	// case country.USA:
	// 	sc.iraq.GetMessage(m)
	// case country.Iraq:
	// 	sc.usa.GetMessage(m)
	// default:
	// 	fmt.Println("Illegal country!")
	// }

	if _, ok := c.(country.USA); ok {
		sc.iraq.GetMessage(m)
	} else if _, ok := c.(country.Iraq); ok {
		sc.usa.GetMessage(m)
	} else {
		fmt.Println("Illegal country!")
	}

}

func (sc SecurityCouncil) SetCountry(usa country.USA, iraq country.Iraq) {
	sc.usa = usa
	sc.iraq = iraq
}