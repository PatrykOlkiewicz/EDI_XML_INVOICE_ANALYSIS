CREATE TABLE Buyer(
    Buyer_TaxID           nvarchar(255) NULL,
    BuyerId               nvarchar(255) NULL,
    Buyer_Name            nvarchar(255) NULL,
    Buyer_StreetAndNumber nvarchar(255) NULL,
    Buyer_CityName        nvarchar(255) NULL,
    Buyer_PostalCode      nvarchar(255) NULL,
    Buyer_Country         nvarchar(255) NULL 
);
	
CREATE TABLE Seller( 
    Seller_TaxID           nvarchar(255) NULL,
    SellerId               nvarchar(255) NULL,
    Seller_Name            nvarchar(255) NULL,
    Seller_StreetAndNumber nvarchar(255) NULL,
    Seller_CityName        nvarchar(255) NULL,
    Seller_PostalCode      nvarchar(255) NULL,
    Seller_Country         nvarchar(255) NULL
);

CREATE TABLE Invoice(
    InvoiceNumber           nvarchar(255) NULL,
    InvoiceId               nvarchar(255) NULL,
    InvoiceDate             nvarchar(255) NULL,
    SalesDate               nvarchar(255) NULL,
    InvoiceCurrency         nvarchar(50)  NULL,
    InvoicePaymentDueDate   nvarchar(255) NULL,
    InvoicePaymentTerms     nvarchar(255) NULL,
    DocumentFunctionCode    nvarchar(50)  NULL,
    BuyerID_BuyerId         nvarchar(255) NULL, 
    SellerID_SellerId       nvarchar(255) NULL  
); 

CREATE TABLE InvoiceLine(
    Invoice_InvoiceId          nvarchar(255) NULL, 
    LineNumber                 nvarchar(255) NULL,
    SupplierItemCode           nvarchar(255) NULL,
    ItemDescription            nvarchar(255) NULL,
    ItemType                   nvarchar(50)  NULL,
    InvoiceQuantity            nvarchar(255) NULL,
    UnitOfMeasure              nvarchar(50)  NULL,
    TaxRate                    nvarchar(255) NULL,
    InvoiceUnitNetPriceNEW     nvarchar(255) NULL
);  
