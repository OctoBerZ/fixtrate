import typing as t
import typing_extensions as te
from collections import OrderedDict
import datetime as dt
from decimal import Decimal

from fixtrate.message import FixMessage
from .types import FixTag as FT, TYPE_MAP
from .validate import validate, convert, cast as _cast


class IOI(FixMessage):

    _msg_type = "6"

    _fields = OrderedDict({
        FT.IOIid: True,
        FT.IOITransType: True,
        FT.IOIRefID: False,
        FT.Symbol: True,
        FT.SymbolSfx: False,
        FT.SecurityID: False,
        FT.IDSource: False,
        FT.SecurityType: False,
        FT.MaturityMonthYear: False,
        FT.MaturityDay: False,
        FT.PutOrCall: False,
        FT.StrikePrice: False,
        FT.OptAttribute: False,
        FT.ContractMultiplier: False,
        FT.CouponRate: False,
        FT.SecurityExchange: False,
        FT.Issuer: False,
        FT.EncodedIssuerLen: False,
        FT.EncodedIssuer: False,
        FT.SecurityDesc: False,
        FT.EncodedSecurityDescLen: False,
        FT.EncodedSecurityDesc: False,
        FT.Side: True,
        FT.IOIShares: True,
        FT.Price: False,
        FT.Currency: False,
        FT.ValidUntilTime: False,
        FT.IOIQltyInd: False,
        FT.IOINaturalFlag: False,
        FT.NoIOIQualifiers: False,
        FT.IOIQualifier: False,
        FT.Text: False,
        FT.EncodedTextLen: False,
        FT.EncodedText: False,
        FT.TransactTime: False,
        FT.URLLink: False,
        FT.NoRoutingIDs: False,
        FT.RoutingType: False,
        FT.RoutingID: False,
        FT.SpreadToBenchmark: False,
        FT.Benchmark: False,
    })

    def __init__(
        self,
        io_iid: str,
        ioi_trans_type: str,
        symbol: str,
        side: str,
        ioi_shares: str,
    ) -> None:
        super().__init__()
        self.append_pair(35, self._msg_type)
        self.append_pair(
            FT.IOIid,
            convert("STRING", io_iid),
        )
        self.append_pair(
            FT.IOITransType,
            convert("CHAR", ioi_trans_type),
        )
        self.append_pair(
            FT.Symbol,
            convert("STRING", symbol),
        )
        self.append_pair(
            FT.Side,
            convert("CHAR", side),
        )
        self.append_pair(
            FT.IOIShares,
            convert("STRING", ioi_shares),
        )

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOIid]) -> str:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOITransType]) -> str:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Symbol]) -> str:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Side]) -> str:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOIShares]) -> str:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOIRefID]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SymbolSfx]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SecurityID]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IDSource]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SecurityType]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.MaturityMonthYear]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.MaturityDay]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.PutOrCall]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.StrikePrice]) -> t.Optional[Decimal]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.OptAttribute]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.ContractMultiplier]) -> t.Optional[float]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.CouponRate]) -> t.Optional[float]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SecurityExchange]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Issuer]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedIssuerLen]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedIssuer]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SecurityDesc]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedSecurityDescLen]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedSecurityDesc]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Price]) -> t.Optional[Decimal]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Currency]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.ValidUntilTime]) -> t.Optional[dt.datetime]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOIQltyInd]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOINaturalFlag]) -> t.Optional[bool]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.NoIOIQualifiers]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.IOIQualifier]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Text]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedTextLen]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.EncodedText]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.TransactTime]) -> t.Optional[dt.datetime]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.URLLink]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.NoRoutingIDs]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.RoutingType]) -> t.Optional[int]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.RoutingID]) -> t.Optional[str]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.SpreadToBenchmark]) -> t.Optional[Decimal]:
        ...

    @t.overload  # NOQA
    def get(self, tag: te.Literal[FT.Benchmark]) -> t.Optional[str]:
        ...

    def get(self, tag: FT):  # NOQA
        is_required = self._fields[tag]
        val = self.get_raw(tag)
        if val is None:
            if is_required:
                raise ValueError
            return None
        return validate(TYPE_MAP[tag], val)

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOIid],
        val: str,
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOITransType],
        val: str,
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOIRefID],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Symbol],
        val: str,
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SymbolSfx],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SecurityID],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IDSource],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SecurityType],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.MaturityMonthYear],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.MaturityDay],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.PutOrCall],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.StrikePrice],
        val: t.Optional[Decimal],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.OptAttribute],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.ContractMultiplier],
        val: t.Optional[float],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.CouponRate],
        val: t.Optional[float],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SecurityExchange],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Issuer],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedIssuerLen],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedIssuer],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SecurityDesc],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedSecurityDescLen],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedSecurityDesc],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Side],
        val: str,
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOIShares],
        val: str,
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Price],
        val: t.Optional[Decimal],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Currency],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.ValidUntilTime],
        val: t.Optional[dt.datetime],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOIQltyInd],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOINaturalFlag],
        val: t.Optional[bool],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.NoIOIQualifiers],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.IOIQualifier],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Text],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedTextLen],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.EncodedText],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.TransactTime],
        val: t.Optional[dt.datetime],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.URLLink],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.NoRoutingIDs],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.RoutingType],
        val: t.Optional[int],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.RoutingID],
        val: t.Optional[str],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.SpreadToBenchmark],
        val: t.Optional[Decimal],
    ) -> None:
        ...

    @t.overload  # NOQA
    def append(
        self,
        tag: te.Literal[FT.Benchmark],
        val: t.Optional[str],
    ) -> None:
        ...

    def append(self, tag: FT, val: t.Any):  # NOQA
        if tag is FT.IOIid:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.IOITransType:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        elif tag is FT.IOIRefID:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.Symbol:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.SymbolSfx:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.SecurityID:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.IDSource:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.SecurityType:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.MaturityMonthYear:
            assert isinstance(val, str)
            converted = convert("MONTHYEAR", val)
        elif tag is FT.MaturityDay:
            assert isinstance(val, int)
            converted = convert("DAYOFMONTH", val)
        elif tag is FT.PutOrCall:
            assert isinstance(val, int)
            converted = convert("INT", val)
        elif tag is FT.StrikePrice:
            assert isinstance(val, Decimal)
            converted = convert("PRICE", val)
        elif tag is FT.OptAttribute:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        elif tag is FT.ContractMultiplier:
            assert isinstance(val, float)
            converted = convert("FLOAT", val)
        elif tag is FT.CouponRate:
            assert isinstance(val, float)
            converted = convert("FLOAT", val)
        elif tag is FT.SecurityExchange:
            assert isinstance(val, str)
            converted = convert("EXCHANGE", val)
        elif tag is FT.Issuer:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.EncodedIssuerLen:
            assert isinstance(val, int)
            converted = convert("LENGTH", val)
        elif tag is FT.EncodedIssuer:
            assert isinstance(val, str)
            converted = convert("DATA", val)
        elif tag is FT.SecurityDesc:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.EncodedSecurityDescLen:
            assert isinstance(val, int)
            converted = convert("LENGTH", val)
        elif tag is FT.EncodedSecurityDesc:
            assert isinstance(val, str)
            converted = convert("DATA", val)
        elif tag is FT.Side:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        elif tag is FT.IOIShares:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.Price:
            assert isinstance(val, Decimal)
            converted = convert("PRICE", val)
        elif tag is FT.Currency:
            assert isinstance(val, str)
            converted = convert("CURRENCY", val)
        elif tag is FT.ValidUntilTime:
            assert isinstance(val, dt.datetime)
            converted = convert("UTCTIMESTAMP", val)
        elif tag is FT.IOIQltyInd:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        elif tag is FT.IOINaturalFlag:
            assert isinstance(val, bool)
            converted = convert("BOOLEAN", val)
        elif tag is FT.NoIOIQualifiers:
            assert isinstance(val, int)
            converted = convert("INT", val)
        elif tag is FT.IOIQualifier:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        elif tag is FT.Text:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.EncodedTextLen:
            assert isinstance(val, int)
            converted = convert("LENGTH", val)
        elif tag is FT.EncodedText:
            assert isinstance(val, str)
            converted = convert("DATA", val)
        elif tag is FT.TransactTime:
            assert isinstance(val, dt.datetime)
            converted = convert("UTCTIMESTAMP", val)
        elif tag is FT.URLLink:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.NoRoutingIDs:
            assert isinstance(val, int)
            converted = convert("INT", val)
        elif tag is FT.RoutingType:
            assert isinstance(val, int)
            converted = convert("INT", val)
        elif tag is FT.RoutingID:
            assert isinstance(val, str)
            converted = convert("STRING", val)
        elif tag is FT.SpreadToBenchmark:
            assert isinstance(val, Decimal)
            converted = convert("PRICEOFFSET", val)
        elif tag is FT.Benchmark:
            assert isinstance(val, str)
            converted = convert("CHAR", val)
        else:
            raise ValueError(f"{tag} is not a valid FIX tag")
        self.append_pair(tag, converted)

    @classmethod
    def cast(cls, msg: FixMessage) -> "IOI":
        return _cast(cls, msg)