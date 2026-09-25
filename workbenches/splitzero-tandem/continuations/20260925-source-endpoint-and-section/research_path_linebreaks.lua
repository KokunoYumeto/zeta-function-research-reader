-- Typesetting only: preserve complete path/hash text while allowing line breaks.
function Str(el)
  if #el.text > 26 and
     (el.text:match("%.md[.,;]?$") or el.text:match("%.tex[.,;]?$")
      or el.text:match("^[A-Fa-f0-9]+[.,;]?$")) and
     not el.text:match("[{}\\]") then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")
  end
end
function Code(el)
  if #el.text > 26 and not el.text:match("[{}\\]") then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")
  end
end
