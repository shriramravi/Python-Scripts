var excel = new ActiveXObject("Excel.Application");

var excel_file = excel.Workbooks.Open("./text_sri.xlsx");

var excel_sheet = excel_file.Worksheets("Sheet1");

var data = excel_sheet.Cells(1,1).Value = "test";
