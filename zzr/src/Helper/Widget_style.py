commandlink_button_style = '''
QCommandLinkButton:hover{
    background-color: rgba(98, 230, 230, 0.2);
}

QCommandLinkButton:pressed{
    background-color: rgba(255, 255, 255, 0.3);
}

QHeaderView::section, QTableCornerButton::section 
{
    padding: 1px;border: none;
    border-bottom: 1px solid rgb(75, 120, 154);
    border-right: 1px solid rgb(75, 120, 154);
    border-bottom: 1px solid gray;
    background-color:rgba(75, 120, 154, 1);
}

QHeaderView::section
{
    font-size:14px;
    font-family:"Microsoft YaHei";
    background-color: transparent;
    border:none;
    text-align:left;
    margin-left:0px;
    padding-left:0px;
}

QTableWidget::item
{
    border-bottom:1px solid #EEF1F7 ;
}

QTableWidget::item::selected
{
    color:red;
    background: rgba(74, 218, 218, 0.2);
}'''