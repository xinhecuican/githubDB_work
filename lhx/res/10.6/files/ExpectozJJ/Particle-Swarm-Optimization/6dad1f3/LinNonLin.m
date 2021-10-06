function SqError = LinNonLin(X)
a=X(1); b=X(2); c=X(3); d=X(4);

T=importCSV();

Y=a*(log(b+exp(c*(T.Area)-d)));
SqError = sum((Y-T.Species).^2);
end                                                                                                                           