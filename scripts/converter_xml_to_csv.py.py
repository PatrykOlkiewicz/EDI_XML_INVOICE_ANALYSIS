# Script converts EDI XML files from Comarch ERP into a single CSV file.



import os
import xml.etree.ElementTree as ET
import csv

# Paths
folder_xml = r"D:\Dane Comarch"
folder_csv = r"D:\Dane Comarch CSV"
csv_file = os.path.join(folder_csv, "all_invoices.csv")

# Create destination folder if it doesn't exist
os.makedirs(folder_csv, exist_ok=True)

with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    # Open CSV writer without pre-defined headers (they will be inferred from first row)
    writer = None

    # Walk through all XML files
    for root_dir, dirs, files in os.walk(folder_xml):
        for file in files:
            if file.lower().endswith(".xml"):
                file_path = os.path.join(root_dir, file)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    # Invoice header
                    header = root.find('Invoice-Header')
                    invoice_number = header.findtext('InvoiceNumber', default='').strip()
                    invoice_date = header.findtext('InvoiceDate', default='').strip()
                    sales_date = header.findtext('SalesDate', default='').strip()
                    invoice_currency = header.findtext('InvoiceCurrency', default='').strip()
                    payment_due = header.findtext('InvoicePaymentDueDate', default='').strip()
                    payment_terms = header.findtext('InvoicePaymentTerms', default='').strip()
                    doc_func = header.findtext('DocumentFunctionCode', default='').strip()

                    # Buyer
                    buyer = root.find('Invoice-Parties/Buyer')
                    buyer_taxid = buyer.findtext('TaxID', default='').strip()
                    buyer_name = buyer.findtext('Name', default='').strip()
                    buyer_street = buyer.findtext('StreetAndNumber', default='').strip()
                    buyer_city = buyer.findtext('CityName', default='').strip()
                    buyer_postal = buyer.findtext('PostalCode', default='').strip()
                    buyer_country = buyer.findtext('Country', default='').strip()

                    # Seller
                    seller = root.find('Invoice-Parties/Seller')
                    seller_taxid = seller.findtext('TaxID', default='').strip()
                    seller_name = seller.findtext('Name', default='').strip()
                    seller_street = seller.findtext('StreetAndNumber', default='').strip()
                    seller_city = seller.findtext('CityName', default='').strip()
                    seller_postal = seller.findtext('PostalCode', default='').strip()
                    seller_country = seller.findtext('Country', default='').strip()

                    # Invoice lines
                    lines = root.findall('Invoice-Lines/Line')
                    for line in lines:
                        line_item = line.find('Line-Item')
                        row = {
                            "InvoiceNumber": invoice_number,
                            "InvoiceDate": invoice_date,
                            "SalesDate": sales_date,
                            "InvoiceCurrency": invoice_currency,
                            "InvoicePaymentDueDate": payment_due,
                            "InvoicePaymentTerms": payment_terms,
                            "DocumentFunctionCode": doc_func,
                            "Buyer_TaxID": buyer_taxid,
                            "Buyer_Name": buyer_name,
                            "Buyer_StreetAndNumber": buyer_street,
                            "Buyer_CityName": buyer_city,
                            "Buyer_PostalCode": buyer_postal,
                            "Buyer_Country": buyer_country,
                            "Seller_TaxID": seller_taxid,
                            "Seller_Name": seller_name,
                            "Seller_StreetAndNumber": seller_street,
                            "Seller_CityName": seller_city,
                            "Seller_PostalCode": seller_postal,
                            "Seller_Country": seller_country,
                            "LineNumber": line_item.findtext('LineNumber', default='').strip(),
                            "SupplierItemCode": line_item.findtext('SupplierItemCode', default='').strip(),
                            "ItemDescription": line_item.findtext('ItemDescription', default='').strip(),
                            "ItemType": line_item.findtext('ItemType', default='').strip(),
                            "InvoiceQuantity": line_item.findtext('InvoiceQuantity', default='').strip(),
                            "UnitOfMeasure": line_item.findtext('UnitOfMeasure', default='').strip(),
                            "InvoiceUnitNetPrice": line_item.findtext('InvoiceUnitNetPrice', default='').strip(),
                            "TaxRate": line_item.findtext('TaxRate', default='').strip(),
                            "TaxAmount": line_item.findtext('TaxAmount', default='').strip(),
                            "NetAmount": line_item.findtext('NetAmount', default='').strip()
                        }

                        # Initialize CSV writer with headers on first row
                        if writer is None:
                            writer = csv.DictWriter(f, fieldnames=row.keys())
                            writer.writeheader()
                        
                        writer.writerow(row)

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

print("Conversion completed. CSV file ready at:", csv_file)
