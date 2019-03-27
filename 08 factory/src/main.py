import operator_factory as opf


def main():
    number_a, number_b = 10, 5

    op_factory = opf.AddFactory()
    op = op_factory.create_operator()
    print "Concrete Factory is AddFactory, %s + %s = %s" \
          % (number_a, number_b, op.get_result(number_a, number_b))

    # only need to modify the type of concrete factory class
    op_factory = opf.SubFactory()
    op = op_factory.create_operator()
    print "Concrete Factory is SubFactory, %s - %s = %s" \
          % (number_a, number_b, op.get_result(number_a, number_b))

    # only need to modify the type of concrete factory class
    op_factory = opf.MulFactory()
    op = op_factory.create_operator()
    print "Concrete Factory is MulFactory, %s * %s = %s" \
          % (number_a, number_b, op.get_result(number_a, number_b))

    # only need to modify the type of concrete factory class
    op_factory = opf.DivFactory()
    op = op_factory.create_operator()
    print "Concrete Factory is DivFactory, %s / %s = %s" \
          % (number_a, number_b, op.get_result(number_a, number_b))


main()
