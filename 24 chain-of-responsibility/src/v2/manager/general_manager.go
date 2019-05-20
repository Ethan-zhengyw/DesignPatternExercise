package manager

import "fmt"
import "v2/request"

type GeneralManager struct {
    Super AbstractManager
}

func (m GeneralManager) ProcessRequest(r request.Request) bool {
	result := false
	if (r.Type == request.Leave) || 
	       (r.Type == request.Salary && r.Amount <= 500) {
		fmt.Println(m, "approve request:", r)
		result = true
	}
	return result
}