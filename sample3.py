from flet import *

def main(page : Page):
    page.title = "Electric Bill calculator"
    page.bgcolor = colors.WHITE54
    page.window_height = 1000
    page.window_width = 700
    page.spacing = 50
    page.window_center()
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    def calculate(e):
        kwh_used = float(kilo.value)
        rate = float(radio_btns.value)
        gen_rate = 0.02 if rate == 12 else 0.05
        trans_rate = 0.01 if rate == 12 else 0.02
        other_charges = 230 if rate == 12 else 450
        after_due_date_charges = {
            0: 0,
            1: 0,
            2: 200,
            3: 300,
            4: 500,
        }[int(dropdown_due_date.value)]
        gen_charge = kwh_used * rate * gen_rate
        trans_charge = kwh_used * rate * trans_rate
        final_bill = kwh_used * rate + after_due_date_charges + other_charges + gen_charge + trans_charge
        gen_charges.value = f"{gen_charge:.2f}"
        trans_charges.value = f"{trans_charge:.2f}"
        other_charge.value = f"{other_charges:.2f}"
        txt.value = f"Final Bill: {final_bill:.2f}"
        page.update()


    kilo = TextField(value = 0, label = "Kilowatt hour used", on_change = calculate, width=300)
    gen_charges = TextField(value = 0, label = "Generation Charge", on_change = calculate, width=300)
    other_charge = TextField(value = 0, label = "Other Charges", on_change = calculate, width=300)

    radio_btns = RadioGroup(content = Row(controls = [
        Radio(value = 12, label = "Residential"),
        Radio(value = 15, label = "Commercial")
    ], width=300), value = 12, on_change = calculate)

    trans_charges = TextField(value = 0, label = "Transmission Charge", on_change = calculate, width=300)
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
                ], value = 0, on_change = calculate, width=300)

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
    

    row1 = Row(controls = [
        kilo,
        radio_btns
    ], alignment = MainAxisAlignment.SPACE_EVENLY, spacing = 50)

    row2 = Row(controls = [
        gen_charges,
        trans_charges
    ], alignment = MainAxisAlignment.SPACE_EVENLY, spacing = 50)

    row3 = Row(controls = [
        other_charge,
        dropdown_due_date
    ], alignment = MainAxisAlignment.SPACE_EVENLY, spacing = 50)

    col = Column(controls = [
        row1,
        row2,
        row3
    ], alignment = CrossAxisAlignment.CENTER, spacing = 50)


    page.add(c1, col, txt)
    page.update()

app(target = main)
