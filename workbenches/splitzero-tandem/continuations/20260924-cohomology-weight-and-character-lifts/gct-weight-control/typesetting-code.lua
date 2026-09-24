-- Preserve code and source-locator text while allowing typographic line breaks.
function Code(el)
  if #el.text > 26 and not el.text:match("[{}\\]") then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")
  end
end
function Str(el)
  if #el.text >= 40 and el.text:match("^[A-Fa-f0-9]+[.,;]?$" ) then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")
  end
end
