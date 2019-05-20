package main

import (
    "fmt"
    "v1/manager"
    "v1/request"
)

func main() {
    var mArr []manager.Manager
    mBasicManager := manager.Manager{"mBasicManager", manager.BasicManager}
    mDirector := manager.Manager{"mDirector", manager.Director}
    mGeneralManager := manager.Manager{"mGeneralManager", manager.GeneralManager}
    mArr = append(mArr, mBasicManager)
    mArr = append(mArr, mDirector)
    mArr = append(mArr, mGeneralManager)

    var rArr []request.Request
    rLeave_2 := request.Request{request.Leave, "Hello, I need to leave for 2 day.", 2}
    rLeave_5 := request.Request{request.Leave, "Hello, I need to leave for 5 day.", 5}
    rLeave_10 := request.Request{request.Leave, "Hello, I need to leave for 10 day.", 10}
    rSalary_500 := request.Request{request.Salary, "Hello, I hope to have salary raised for 500$.", 500}
    rSalary_1000 := request.Request{request.Salary, "Hello, I hope to have salary raised for 1000$.", 1000}
    rArr = append(rArr, rLeave_2)
    rArr = append(rArr, rLeave_5)
    rArr = append(rArr, rLeave_10)
    rArr = append(rArr, rSalary_500)
    rArr = append(rArr, rSalary_1000)

    for _, m := range mArr {
        for _, r := range rArr {
            result := m.ProcessRequest(r)
            fmt.Println("Manager", m, "processing request", r, "result:", result)
        }
        fmt.Println()
    }
}

