package country

type ICountry interface {
    SendMessage(message string)
    GetMessage(message string)
    SetMediator(mediator *IUnitedNations)
}

type IUnitedNations interface {
    sendMessage(message string, country ICountry)
}
