return {
  'gleachkr/lectic',
  name = 'lectic.nvim',
  config = function(plugin)
    vim.opt.rtp:append(plugin.dir .. "/extra/lectic.nvim")
  end
}
