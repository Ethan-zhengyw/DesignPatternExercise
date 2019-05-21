package country

import "fmt"

type USA struct {
    mediator IUnitedNations
}

func (usa USA) SendMessage(m string) {
    usa.mediator.sendMessage(m, usa)
}

func (usa USA) GetMessage(m string) {
    fmt.Println("USA get message:", m)
}

func (usa USA) SetMediator(m IUnitedNations) {
    usa.mediator = m
}