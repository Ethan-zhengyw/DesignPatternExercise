package manager

import "v1/request"

type Level int

const (
    BasicManager Level = iota  // can approve leave request <= 2
    Director  // can approve leave request <= 5
    GeneralManager  // can approve leave request,
                    // and salary raise request <= 500
)

type Manager struct {
    Name string
    Level Level
}

func (m Manager) ProcessRequest(r request.Request) bool {
    result := false
    if r.Type == request.Leave {
        // process leave request
        if r.Amount <= 2 {
            result = true
        } else if r.Amount <= 5 && m.Level >= Director {
            result = true
        } else if m.Level == GeneralManager {
            result = true
        }
    } else if r.Type == request.Salary {
        // process salary raise request
        if m.Level == GeneralManager && r.Amount <= 500 {
            result = true
        }
    }
    return result
}
