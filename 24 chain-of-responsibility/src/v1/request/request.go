package request

type Type string
const (
    Leave Type = "LEAVE"
    Salary = "SALARY"
)

type Request struct {
    Type Type
    Contents string
    Amount int
}
