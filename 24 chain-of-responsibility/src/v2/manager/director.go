package manager

import "fmt"
import "v2/request"

type Director struct {
    Super AbstractManager
    Leader *GeneralManager
}

func (m Director) ProcessRequest(r request.Request) bool {
	result := false
	if r.Type == request.Leave && r.Amount <= 5 {
		fmt.Println(m, "approve request:", r)
		result = true
	} else if m.Leader != nil {
		result = m.Leader.ProcessRequest(r)
	}
	return result
}