package manager

import "v2/request"

type Level int

const (
    L_BasicManager Level = iota  // can approve leave request <= 2
    L_Director  // can approve leave request <= 5
    L_GeneralManager  // can approve leave request,
                    // and salary raise request <= 500
)

type IManager interface {
    ProcessRequest(r request.Request) bool
}

type AbstractManager struct {
    Name string
    Level Level
}

