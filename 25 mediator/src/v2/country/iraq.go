package country

import "fmt"

type Iraq struct {
    mediator *IUnitedNations
}

func (iraq Iraq) SendMessage(m string) {
    iraq.mediator.sendMessage(m, iraq)
}

func (iraq *Iraq) GetMessage(m string) {
    fmt.Println("Iraq get message:", m)
}

func (iraq *Iraq) SetMediator(m *IUnitedNations) {
    iraq.mediator = m
}