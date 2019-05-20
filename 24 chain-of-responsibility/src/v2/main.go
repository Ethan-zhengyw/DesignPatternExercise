package main

import (
    "fmt"
    "v2/manager"
    "v2/request"
)

func main() {
    mGeneralManager := manager.GeneralManager{
        manager.AbstractManager{"mGeneralManager", manager.L_GeneralManager}}
    mDirector := manager.Director{
        manager.AbstractManager{"mDirector", manager.L_Director}, &mGeneralManager}
    mBasicManager := manager.BasicManager{
        manager.AbstractManager{"mBasicManager", manager.L_BasicManager}, &mDirector}

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

    for _, r := range rArr {
        result := mBasicManager.ProcessRequest(r)
        fmt.Println("processing request", r, "result:", result, "\n")
    }
}

