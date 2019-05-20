package manager

import "fmt"
import "v2/request"

type BasicManager struct {
    Super AbstractManager
    Leader *Director
}

func (m BasicManager) ProcessRequest(r request.Request) bool {
	result := false
	if r.Type == request.Leave && r.Amount <= 2 {
		fmt.Println(m, "approve request:", r)
		result = true
	} else if m.Leader != nil {
		result = m.Leader.ProcessRequest(r)
	}
	return result
}