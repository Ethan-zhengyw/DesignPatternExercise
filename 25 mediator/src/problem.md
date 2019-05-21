# Error message:

```
[root@cefbd9b873ff src]# go run v1/main.go 
# command-line-arguments
v1/main.go:13: cannot use sc (type united_nations.SecurityCouncil) as type country.IUnitedNations in argument to usa.SetMediator:
	united_nations.SecurityCouncil does not implement country.IUnitedNations (missing country.sendMessage method)
		have united_nations.sendMessage(string, country.ICountry)
		want country.sendMessage(string, country.ICountry)
v1/main.go:14: cannot use sc (type united_nations.SecurityCouncil) as type country.IUnitedNations in argument to iraq.SetMediator:
	united_nations.SecurityCouncil does not implement country.IUnitedNations (missing country.sendMessage method)
		have united_nations.sendMessage(string, country.ICountry)
		want country.sendMessage(string, country.ICountry)
```
# Question: why united_nations.SecurityCouncil can't be used as type country.IUnitedNations?

I have implemented the sendMessage method for united_nations.SecurityCouncil
```
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
```

maybe get inflenced by the the member of united_nations.SecurityCouncil usa, iraq also have method sendMessage?

# TODO: answer
