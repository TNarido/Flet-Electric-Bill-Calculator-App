from flet import *

def main(page : Page):
    page.title = "Electric Bill calculator"
    page.bgcolor = colors.WHITE54
    page.window_height = 1000
    page.window_width = 700
    page.spacing = 50
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.window_center()

    def compute_charges(rate, kwh_used):
        charge = rate * kwh_used
        gen_charge = charge * 0.02 if rate == 12 else charge * 0.05
        trans_charge = charge * 0.01 if rate == 12 else charge * 0.02
        other_charges = 230 if rate == 12 else 450
        return charge, gen_charge, trans_charge, other_charges

    def calculate(e):
        rate = float(radio_btns.value)
        kwh_used = float(kilo.value)
        charge, gen_charge, trans_charge, other_charges = compute_charges(rate, kwh_used)

        after_due_date_charges = {
            0: 0,
            1: 0,
            2: 200,
            3: 300,
            4: 500
        }
        after_due_date_charge = after_due_date_charges[float(dropdown_due_date.value)]
        final_bill = charge + after_due_date_charge + other_charges + gen_charge + trans_charge

        gen_charges.value = f"{'%0.2f'%(gen_charge)}"
        trans_charges.value = f"{'%0.2f'%(trans_charge)}"
        other_charge.value = f"{'%0.2f'%(other_charges)}"
        txt.value = f"{'Final Bill: %0.2f'%(final_bill)}"
        page.update()


    kilo = TextField(value = 0, label = "Kilowatt hour used", on_change = calculate)
    gen_charges = TextField(value = 0, label = "Generation Charge", on_change = calculate)
    other_charge = TextField(value = 0, label = "Other Charges", on_change = calculate)

    radio_btns = RadioGroup(content = Row(controls = [
        Radio(value = 12, label = "Residential"),
        Radio(value = 15, label = "Commercial")
    ]), value = 0, on_change = calculate)

    trans_charges = TextField(value = 0, label = "Transmission Charge", on_change = calculate)
    dropdown_due_date = Dropdown(label = "After due date charges",
                options = [
                    dropdown.Option(1),
                    dropdown.Option(2),
                    dropdown.Option(3),
                    dropdown.Option(4),
                    dropdown.Option(5),
                    dropdown.Option(6),
                    dropdown.Option(7),
                    dropdown.Option(8)
                ], value = 1, on_change = calculate)

    txt = Text(value = "Final Bill: ", size = 50, weight = FontWeight.BOLD)

    c1 = Container(
        content = Text("Electric Bill Calculator", size = 40, weight = FontWeight.BOLD),
        bgcolor = colors.BLACK,
        padding = 5,
        alignment = alignment.top_center,
        border = border.all(1.0, colors.BLACK),
        gradient = LinearGradient(
            begin = alignment.center_right,
            end = alignment.center_left,
            colors = [colors.BLACK, colors.WHITE, colors.BLACK]
        ),
        margin = margin.only(bottom = 80),
        height = 70,
        width = 500
    )
    

    col1 = Column(controls = [
        kilo,
        gen_charges,
        other_charge
    ], 
    horizontal_alignment = CrossAxisAlignment.CENTER,
    spacing = 50
    )

    col2 = Column(controls = [
        radio_btns,
        trans_charges,
        dropdown_due_date
    ],
    horizontal_alignment = CrossAxisAlignment.CENTER,
    spacing = 50
    )

    row1 = Row(controls = [
        col1,
        col2
    ],
    alignment = MainAxisAlignment.SPACE_EVENLY)


    page.add(c1, row1, txt)
    page.update()

app(target = main)